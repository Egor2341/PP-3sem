from fastapi import APIRouter, HTTPException, status
def user_is_not_on_project():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="User is not found on this project!")