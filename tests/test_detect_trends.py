#!/usr/bin/env python3
"""Unit tests for scripts/detect_trends.py"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

import unittest
from detect_trends import (
    normalize_url,
    tokenize,
    extract_keywords,
    compute_title_similarity,
    compute_keyword_overlap,
    build_similarity_graph,
    find_clusters,
    generate_cluster_label,
    compute_trend_score,
)


class TestNormalizeUrl(unittest.TestCase):

    def test_strips_utm_params(self):
        url = 'https://example.com/article?utm_source=newsletter&utm_medium=email&id=42'
        result = normalize_url(url)
        self.assertNotIn('utm_source', result)
        self.assertNotIn('utm_medium', result)
        self.assertIn('id=42', result)

    def test_strips_www(self):
        url = 'https://www.example.com/article'
        self.assertEqual(normalize_url(url), 'https://example.com/article')

    def test_strips_trailing_slash(self):
        url = 'https://example.com/article/'
        self.assertEqual(normalize_url(url), 'https://example.com/article')

    def test_forces_https(self):
        url = 'http://example.com/article'
        self.assertEqual(normalize_url(url), 'https://example.com/article')

    def test_identical_urls_after_normalization(self):
        a = 'http://www.example.com/post/?utm_source=tldr&utm_campaign=ai'
        b = 'https://example.com/post'
        self.assertEqual(normalize_url(a), normalize_url(b))

    def test_preserves_path(self):
        url = 'https://example.com/blog/2026/03/ai-trends'
        self.assertEqual(normalize_url(url), 'https://example.com/blog/2026/03/ai-trends')

    def test_keeps_non_utm_params(self):
        url = 'https://example.com/search?q=ai&page=2'
        result = normalize_url(url)
        self.assertIn('q=ai', result)
        self.assertIn('page=2', result)


class TestTokenize(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(tokenize('Hello World'), ['hello', 'world'])

    def test_filters_short_tokens(self):
        result = tokenize('I am an AI developer')
        self.assertNotIn('am', result)
        self.assertNotIn('an', result)

    def test_handles_accents(self):
        result = tokenize('réseau neuronal profond')
        self.assertIn('réseau', result)
        self.assertIn('neuronal', result)


class TestExtractKeywords(unittest.TestCase):

    def test_returns_set(self):
        result = extract_keywords('AI and machine learning', 'deep learning models')
        self.assertIsInstance(result, set)

    def test_excludes_stopwords(self):
        result = extract_keywords('The new AI model', 'This is a test of the system')
        self.assertNotIn('the', result)
        self.assertNotIn('this', result)

    def test_title_weighted(self):
        result = extract_keywords('transformers', 'a' * 2000)
        self.assertIn('transformers', result)

    def test_respects_top_n(self):
        text = ' '.join(f'word{i}' * (20 - i) for i in range(20))
        result = extract_keywords('', text, top_n=5)
        self.assertLessEqual(len(result), 5)


class TestComputeTitleSimilarity(unittest.TestCase):

    def test_identical_titles(self):
        score = compute_title_similarity('GPT-5 launch today', 'GPT-5 launch today')
        self.assertEqual(score, 1.0)

    def test_completely_different(self):
        score = compute_title_similarity('Kubernetes best practices', 'French cooking recipes')
        self.assertEqual(score, 0.0)

    def test_partial_overlap(self):
        score = compute_title_similarity(
            'OpenAI launches GPT-5 model',
            'GPT-5 model performance benchmarks'
        )
        self.assertGreater(score, 0.0)
        self.assertLess(score, 1.0)

    def test_empty_title(self):
        score = compute_title_similarity('', 'Something')
        self.assertEqual(score, 0.0)

    def test_stopwords_ignored(self):
        # "The" and "of" are stopwords, shouldn't inflate similarity
        score = compute_title_similarity(
            'The art of cooking pasta',
            'The art of debugging code'
        )
        # Only "art" overlaps after stopword removal
        self.assertLess(score, 0.5)

    def test_threshold_scenario(self):
        # Simulating the ≥0.4 threshold from the plan
        score = compute_title_similarity(
            'GPT-5 released with new capabilities',
            'GPT-5 new model released by OpenAI'
        )
        self.assertGreaterEqual(score, 0.4)


class TestComputeKeywordOverlap(unittest.TestCase):

    def test_full_overlap(self):
        a = {'ai', 'model', 'training'}
        b = {'ai', 'model', 'training', 'inference'}
        self.assertEqual(compute_keyword_overlap(a, b), 1.0)

    def test_no_overlap(self):
        a = {'python', 'django', 'web'}
        b = {'rust', 'compiler', 'memory'}
        self.assertEqual(compute_keyword_overlap(a, b), 0.0)

    def test_partial_overlap(self):
        a = {'ai', 'model', 'training', 'data'}
        b = {'ai', 'model', 'inference', 'cloud'}
        score = compute_keyword_overlap(a, b)
        self.assertAlmostEqual(score, 0.5)

    def test_empty_sets(self):
        self.assertEqual(compute_keyword_overlap(set(), {'a'}), 0.0)
        self.assertEqual(compute_keyword_overlap({'a'}, set()), 0.0)
        self.assertEqual(compute_keyword_overlap(set(), set()), 0.0)


class TestBuildSimilarityGraph(unittest.TestCase):

    def _make_source(self, index, title, newsletter, url=''):
        return {
            'index': index,
            'title': title,
            'newsletter': newsletter,
            'url': url or f'https://example.com/{index}',
            'theme': 'IA',
        }

    def test_same_newsletter_no_edge(self):
        sources = [
            self._make_source(0, 'GPT-5 launch', 'Newsletter A'),
            self._make_source(1, 'GPT-5 launch', 'Newsletter A'),
        ]
        graph = build_similarity_graph(sources, {})
        self.assertEqual(graph[0], set())
        self.assertEqual(graph[1], set())

    def test_cross_newsletter_url_match(self):
        url = 'https://example.com/gpt5-article'
        sources = [
            self._make_source(0, 'Article A', 'Newsletter A', url),
            self._make_source(1, 'Article B', 'Newsletter B', url),
        ]
        graph = build_similarity_graph(sources, {})
        self.assertIn(1, graph[0])
        self.assertIn(0, graph[1])

    def test_cross_newsletter_title_match(self):
        sources = [
            self._make_source(0, 'GPT-5 launched with new capabilities', 'Newsletter A'),
            self._make_source(1, 'GPT-5 new capabilities launched today', 'Newsletter B'),
        ]
        graph = build_similarity_graph(sources, {})
        self.assertIn(1, graph[0])

    def test_no_edge_below_thresholds(self):
        sources = [
            self._make_source(0, 'Kubernetes scaling patterns', 'Newsletter A'),
            self._make_source(1, 'French pastry techniques', 'Newsletter B'),
        ]
        graph = build_similarity_graph(sources, {})
        self.assertEqual(graph[0], set())


class TestFindClusters(unittest.TestCase):

    def test_single_component(self):
        graph = {0: {1, 2}, 1: {0}, 2: {0}}
        clusters = find_clusters(graph)
        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0], {0, 1, 2})

    def test_two_components(self):
        graph = {0: {1}, 1: {0}, 2: {3}, 3: {2}, 4: set()}
        clusters = find_clusters(graph)
        self.assertEqual(len(clusters), 2)
        cluster_sets = [frozenset(c) for c in clusters]
        self.assertIn(frozenset({0, 1}), cluster_sets)
        self.assertIn(frozenset({2, 3}), cluster_sets)

    def test_no_edges(self):
        graph = {0: set(), 1: set(), 2: set()}
        clusters = find_clusters(graph)
        self.assertEqual(len(clusters), 0)

    def test_chain(self):
        graph = {0: {1}, 1: {0, 2}, 2: {1, 3}, 3: {2}}
        clusters = find_clusters(graph)
        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0], {0, 1, 2, 3})


class TestGenerateClusterLabel(unittest.TestCase):

    def test_label_from_common_terms(self):
        sources = [
            {'title': 'GPT-5 launch announcement'},
            {'title': 'GPT-5 performance benchmarks'},
            {'title': 'OpenAI GPT-5 release'},
        ]
        label = generate_cluster_label(sources)
        self.assertIn('gpt', label)

    def test_empty_cluster(self):
        label = generate_cluster_label([])
        self.assertEqual(label, 'trend')


class TestComputeTrendScore(unittest.TestCase):

    def _make_source(self, index, title, newsletter, url=''):
        return {
            'index': index,
            'title': title,
            'newsletter': newsletter,
            'url': url or f'https://example.com/{index}',
            'theme': 'IA',
        }

    def _precompute(self, sources, contents=None):
        """Precompute norm_urls and keywords like detect_trends does."""
        contents = contents or {}
        norm_urls = [normalize_url(s['url']) for s in sources]
        keywords = [extract_keywords(s['title'], contents.get(s['index'], '')) for s in sources]
        return norm_urls, keywords

    def test_url_match_gives_high_score(self):
        url = 'https://example.com/same-article'
        sources = [
            self._make_source(0, 'Article A', 'NL-A', url),
            self._make_source(1, 'Article B', 'NL-B', url),
        ]
        norm_urls, keywords = self._precompute(sources)
        score = compute_trend_score(0, sources, {0, 1}, norm_urls, keywords)
        self.assertGreaterEqual(score, 0.5)

    def test_same_newsletter_ignored(self):
        url = 'https://example.com/same-article'
        sources = [
            self._make_source(0, 'Article A', 'Same NL', url),
            self._make_source(1, 'Article B', 'Same NL', url),
        ]
        norm_urls, keywords = self._precompute(sources)
        score = compute_trend_score(0, sources, {0, 1}, norm_urls, keywords)
        self.assertEqual(score, 0.0)

    def test_score_capped_at_one(self):
        url = 'https://example.com/same'
        sources = [
            self._make_source(0, 'GPT-5 launch new model', 'NL-A', url),
            self._make_source(1, 'GPT-5 launch new model', 'NL-B', url),
        ]
        contents = {0: 'artificial intelligence machine learning deep neural network transformer model training inference optimization deployment scaling',
                     1: 'artificial intelligence machine learning deep neural network transformer model training inference optimization deployment scaling'}
        norm_urls, keywords = self._precompute(sources, contents)
        score = compute_trend_score(0, sources, {0, 1}, norm_urls, keywords)
        self.assertLessEqual(score, 1.0)


if __name__ == '__main__':
    unittest.main()
