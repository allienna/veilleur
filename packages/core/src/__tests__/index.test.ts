import { describe, expect, it } from "vitest";
import { VERSION } from "../index";

describe("VERSION", () => {
  it("should be a non-empty string", () => {
    expect(typeof VERSION).toBe("string");
    expect(VERSION.length).toBeGreaterThan(0);
  });

  it("should match semver format", () => {
    expect(VERSION).toMatch(/^\d+\.\d+\.\d+$/);
  });
});
