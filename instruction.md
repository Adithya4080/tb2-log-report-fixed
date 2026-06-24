# Log Report Task

An Apache-style access log is available at `/app/access.log`.

Parse the log and write a JSON report to `/app/report.json`.

## Required output format

The file must be valid JSON with exactly these three keys:

```json
{
  "total_requests": <integer — total number of log lines>,
  "unique_ips":     <integer — count of distinct client IP addresses>,
  "top_path":       <string  — the URL path that appears most often>
}
```

## Success criteria

1. `/app/report.json` exists and is valid JSON.
2. `total_requests` is the exact integer count of log lines in `/app/access.log`.
3. `unique_ips` is the exact integer count of distinct IP addresses in the log.
4. `top_path` is the URL path string with the highest request count in the log.
