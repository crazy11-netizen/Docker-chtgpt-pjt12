                     GitHub
                        │
                   git push
                        │
                        ▼
                  Jenkins (EC2)
                        │
             Checkout Source Code
                        │
                        ▼
               Build Docker Image
                        │
                        ▼
          Push Image to Docker Hub
                        │
                        ▼
          Docker Compose Deployment
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
      Nginx Reverse Proxy         Flask App
                                        │
                                        ▼
                                 MySQL Database
