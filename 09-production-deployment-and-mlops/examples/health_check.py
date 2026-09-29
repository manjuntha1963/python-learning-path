# Purpose: Implement a health check endpoint for production services.
# Health checks verify that an application is running and healthy.

def health_check() -> dict:
    """
    Return the current health status of the application.
    
    Health checks are called by:
    - Load balancers (to remove unhealthy instances)
    - Monitoring systems (to trigger alerts)
    - Deployment tools (to verify successful deployment)
    
    Returns:
        A dictionary with status and version information
    """
    # Status: "healthy" means the app is ready to serve requests
    status = "healthy"
    
    # Version: used to verify that the correct version deployed
    version = "1.0.0"
    
    # Build and return the response
    return {
        "status": status,
        "version": version,
        "message": "Application is running and ready"
    }


# Call the health check
health_status = health_check()

print("Health Check Response:")
print(f"  Status: {health_status['status']}")
print(f"  Version: {health_status['version']}")
print(f"  Message: {health_status['message']}")
print()

print("In production, this endpoint would check:")
print("  - Database connectivity")
print("  - Cache availability")
print("  - External service dependencies")
print("  - Disk space")
print("  - Memory usage")
