from fastapi import HTTPException


def Response(res):
    if res.status_code < 300:
        return res.json()
    else:
        try:
            text = res.json()['detail']  # error response from other APIs
        except BaseException:
            text = res.text
        raise HTTPException(status_code=res.status_code, detail=text)
