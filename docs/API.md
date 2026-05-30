# API Documentation

## Base URL

- Development: `http://localhost:8000`
- Production: Configured via environment

## Authentication

Currently no authentication is implemented. This will be added in future iterations.

## Endpoints

### Health Check

#### GET /health

Check the health status of the API.

**Response:**
```json
{
  "status": "healthy",
  "service": "sutradhar-api"
}
```

### Root

#### GET /

API root endpoint with basic information.

**Response:**
```json
{
  "message": "Sutradhar API",
  "version": "1.0.0",
  "docs": "/docs"
}
```

### API Routes

#### GET /api/health

API health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "sutradhar-api"
}
```

## Interactive Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Future Endpoints

The following endpoints will be implemented in future iterations:

- `POST /api/statements/upload` - Upload bank statements
- `GET /api/statements/{id}` - Retrieve statement details
- `POST /api/analysis/transactions` - Analyze transactions
- `GET /api/investigations/{id}` - Get investigation results
- `POST /api/reports/generate` - Generate reports

## Error Handling

All endpoints return standard HTTP status codes:

- `200` - Success
- `400` - Bad Request
- `404` - Not Found
- `422` - Validation Error
- `500` - Internal Server Error

Error response format:
```json
{
  "detail": "Error message description"
}
```
