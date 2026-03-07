# Start n8n in background (starts Colima if needed)
start-n8n:
    @if ! colima status 2>/dev/null | grep -q "Running"; then \
        echo "Starting Colima..."; \
        colima start --memory 8; \
    fi
    cd n8n && docker-compose up -d

# Restart n8n
restart-n8n:
    cd n8n && docker-compose down && docker-compose up -d
