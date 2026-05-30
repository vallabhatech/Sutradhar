# Test script to run backend tests

Write-Host "Running backend tests..." -ForegroundColor Green

# Run tests in backend container
docker-compose exec backend pytest -v

Write-Host "Tests completed!" -ForegroundColor Green
