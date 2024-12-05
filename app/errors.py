from fastapi import HTTPException, status
def user_already_exists():
    return HTTPException(status_code=status.HTTP_409_CONFLICT,
                         detail="The user already exists")

def tour_already_exists():
    return HTTPException(status_code=status.HTTP_409_CONFLICT,
                         detail="The tour already exists")

def invalid_user():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid user")

def invalid_token():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid token")

def access_is_denied():
    return HTTPException(status_code=403,
                         detail="Not enough rights")

def tour_is_unavailable():
    return HTTPException(status_code=404,
                         detail="Tour is unavailable")