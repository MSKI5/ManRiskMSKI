# API Documentation - Sistem Manajemen Risiko KPPN

## Base URL
```
http://localhost:5000/api
```

## Authentication
Semua endpoint (kecuali login) memerlukan JWT token di header:
```
Authorization: Bearer YOUR_JWT_TOKEN
```

## Endpoints

### 1. Authentication

#### Login
```
POST /auth/login
Content-Type: application/json

{
  "username": "mski_user",
  "password": "password123"
}

Response:
{
  "status": "success",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": "uuid",
    "username": "mski_user",
    "section": "Seksi MSKI",
    "role": "user"
  }
}
```

#### Register (Admin only)
```
POST /auth/register
Authorization: Bearer TOKEN

{
  "username": "new_user",
  "email": "user@kppn.local",
  "password": "password123",
  "full_name": "User Name",
  "role": "user",
  "section": "Seksi MSKI"
}
```

### 2. Risk Data

#### Get All Indicators
```
GET /risiko/indicators

Response:
{
  "status": "success",
  "count": 26,
  "data": [
    {
      "id": 1,
      "indicator_code": "1a-CP-01",
      "indicator_name": "Nilai Kinerja Pelaksanaan Anggaran K/L",
      "p26_initial": 14,
      "r26_target": 10,
      "pic_section": "Seksi MSKI"
    }
  ]
}
```

#### Create Risk Assessment
```
POST /risiko/assessments
Authorization: Bearer TOKEN

{
  "indicator_id": 1,
  "quarter": "Q1",
  "year": 2024,
  "frequency": 3,
  "impact": 4,
  "change_reason": "Dilakukan edukasi satker..."
}

Response:
{
  "status": "success",
  "message": "Risk assessment created",
  "data": {
    "id": "uuid",
    "risk_value": 12,
    "risk_category": "Kuning",
    "status": "draft"
  }
}
```

#### Update Risk Assessment
```
PUT /risiko/assessments/{id}
Authorization: Bearer TOKEN

{
  "frequency": 2,
  "impact": 5,
  "change_reason": "Updated reason..."
}
```

#### Submit Risk Assessment
```
POST /risiko/assessments/{id}/submit
Authorization: Bearer TOKEN

Response:
{
  "status": "success",
  "message": "Risk assessment submitted",
  "data": {
    "status": "submitted",
    "submitted_at": "2024-03-15T10:30:00Z"
  }
}
```

### 3. Reports

#### Get Quarterly Summary
```
GET /laporan/summary?quarter=Q1&year=2024
Authorization: Bearer TOKEN

Response:
{
  "status": "success",
  "data": {
    "quarter": "Q1",
    "total_indicators": 26,
    "completed_indicators": 26,
    "blue_count": 5,
    "green_count": 8,
    "yellow_count": 7,
    "orange_count": 4,
    "red_count": 2,
    "overall_risk_score": 13
  }
}
```

#### Export to Excel
```
GET /laporan/export/excel?quarter=Q1&year=2024
Authorization: Bearer TOKEN

Response: File download (.xlsx)
```

#### Export to PDF
```
GET /laporan/export/pdf?quarter=Q1&year=2024
Authorization: Bearer TOKEN

Response: File download (.pdf)
```

### 4. Matrix & Visualization

#### Get Risk Matrix
```
GET /matriks/matrix?quarter=Q1&year=2024&section=Seksi%20MSKI
Authorization: Bearer TOKEN

Response:
{
  "status": "success",
  "data": {
    "matrix": [
      {"risk_value": 1, "frequency": 1, "impact": 1, "category": "Biru", "color": "#0066CC"},
      ...
    ],
    "indicators_in_matrix": [
      {"indicator_id": 1, "risk_value": 14, "category": "Kuning"}
    ]
  }
}
```

#### Get Change Analysis
```
GET /matriks/analysis?indicator_id=1&from_quarter=Q1&to_quarter=Q2
Authorization: Bearer TOKEN

Response:
{
  "status": "success",
  "data": {
    "indicator": "1a-CP-01",
    "from_value": 14,
    "to_value": 10,
    "change": -4,
    "from_category": "Kuning",
    "to_category": "Hijau",
    "reason": "Edukasi satker...",
    "supporting_docs": ["doc1.pdf", "doc2.xlsx"]
  }
}
```

### 5. Document Management

#### Upload Supporting Document
```
POST /risiko/documents
Authorization: Bearer TOKEN
Content-Type: multipart/form-data

Form data:
- assessment_id: uuid
- document_type: bukti_perubahan
- description: Laporan edukasi satker
- file: [binary file]

Response:
{
  "status": "success",
  "message": "Document uploaded",
  "data": {
    "id": "uuid",
    "original_filename": "Laporan_Edukasi.pdf",
    "file_size": 2345000
  }
}
```

#### Get Documents for Assessment
```
GET /risiko/assessments/{id}/documents
Authorization: Bearer TOKEN

Response:
{
  "status": "success",
  "count": 3,
  "data": [
    {
      "id": "uuid",
      "original_filename": "doc.pdf",
      "uploaded_at": "2024-03-15T10:30:00Z"
    }
  ]
}
```

### 6. Admin Functions

#### Get All Users (Admin only)
```
GET /admin/users
Authorization: Bearer TOKEN

Response:
{
  "status": "success",
  "count": 6,
  "data": [...]
}
```

#### Verify Risk Assessment (Admin only)
```
POST /admin/assessments/{id}/verify
Authorization: Bearer TOKEN

{
  "status": "approved",
  "notes": "Data verified, looks good"
}
```

## Error Responses

```json
{
  "status": "error",
  "message": "Error description",
  "code": 400
}
```

Common error codes:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

## Rate Limiting
```
100 requests per minute per IP
Will return 429 if exceeded
```

## Pagination

Endpoints yang return list support pagination:
```
?page=1&per_page=10
```
