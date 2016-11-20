# coding: cp949
def collisionIntersectRect(_object1, _object2):  # 인터섹렉트 오브젝트 두개
                                                 # 대체 왜 이렇게 하는지 모르겠음
    # 레프트 탑 라이트 바텀
    object1_x1, object1_y1, object1_x2, object1_y2 = _object1.getCollisionBox()  # 오브젝트1 X, Y값
    object2_x1, object2_y1, object2_x2, object2_y2 = _object2.getCollisionBox()  # 오브젝트2 X, Y값
    object3_x1, object3_y1, object3_x2, object3_y2 = 0, 0, 0, 0                  # 오브젝트3 X, Y값 = 0
                                                                                 # 왜 이렇게 했을까

    if (object1_y1 >= object2_y2) and (object1_x2 >= object2_x1) �
            and (object1_x1 <= object2_x2) and (object1_y2 <= object2_y1):  # 오브젝트1의 탑이 오브젝트2의 바텀보다 크고
                                                                             # 오브젝트1의 라이트가 오브젝트2의 레프트보다 크고
                                                                             # 오브젝트1의 레프트가 오브젝트2의 라이트보다 작고
                                                                             # 오브젝트1의 바텀이 오브젝트2의 탑보다 작을 때
                                                                             # 뭔 소리여
        #top
        if object1_y1 < object2_y1:         # 오브젝트1의 탑이 오브젝트2의 탑보다 작을 때
            object3_y1 = object1_y1         # 오브젝트3의 탑 = 오브젝트 1의 탑
        elif object1_y1 >= object2_y1:      # 오브젝트1의 탑이 오브젝트2의 탑보다 클 때
            object3_y1 = object2_y1         # 오브젝트3의 탑 = 오브젝트 2의 탑
                                            # 작은 탑을 오브젝트3의 탑에게 넘겨준다
        #bottom
        if object1_y2 > object2_y2:         # 오브젝트1의 바텀이 오브젝트2의 바텀보다 클 때
            object3_y2 = object1_y2         # 오브젝트3의 바텀 = 오브젝트1의 바텀
        elif object1_y2 <= object2_y2:     # 오브젝트1의 바텀이 오브젝트2의 바텀보다 작을 때
            object3_y2 = object2_y2         # 오브젝트3의 바텀 = 오브젝트2의 바텀
                                            # 큰 바텀을 오브젝트3의 바텀에 넘겨준다
        #right
        if object1_x2 < object2_x2:         # 오브젝트1의 라이트가 오브젝트2의 라이트보다 작을 때
            object3_x2 = object1_x2         # 오브젝트3의 라이트 = 오브젝트1의 라이트
        elif object1_x2 >= object2_x2:      # 오브젝트1의 라이트가 오브젝트2의 라이트보다 클 때
            object3_x2 = object2_x2         # 오브젝트3의 라이트 = 오브젝트2의 라이트
                                            # 작은 라이트를 오브젝트3의 라이트에 넘겨준다
        #left
        if object1_x1 > object2_x1:         # 오브젝트1의 레프트가 오브젝트2의 레프트보다 클 때
            object3_x1 = object1_x1         # 오브젝트3의 레프트 = 오브젝트1의 레프트
        elif object1_x1 <= object2_x1:      # 오브젝트1의 레프트가 오브젝트2의 레프트보다 작을 때
            object3_x1 = object2_x1         # 오브젝트3의 레프트 = 오브젝트2의 레프트
                                            # 큰 레프트를 오브젝트3의 레프트에 넘겨준다
        return True, object3_x1, object3_y1, object3_x2, object3_y2  # 바뀐 오브젝트3의 값 넘긴다
    return False, object3_x1, object3_y1, object3_x2, object3_y2    # 0인 오브젝트3의 값 넘긴다

def collisionPtInRect(_object, _x, _y):  # 피티인렉트 오브젝트 한개, x, y값
    if (_object.X - (int)(_object.sizeX / 2) <= _x) and (_object.X + (int)(_object.sizeX / 2) >= _x):
        if (_object.Y - (int)(_object.sizeY / 2) <= _y) and (_object.Y + (int)(_object.sizeY / 2) >= _y):
            # 오브젝트 안에 _x, _y가 있을 시
            return True
    return False

def collisionAABB(_mainObject, _subObject, _left, _top, _right, _bottom):
    # 메인 오브젝트, 서브오브젝트, 레프트 탑 라이트 바텀
    # 오브젝트3
    if (_right - _left) > (_top - _bottom):
        if _mainObject.Y < _subObject.Y:
            _mainObject.Y -= (_top - _bottom)
        else:
            _mainObject.Y += (_top - _bottom)
    else:
        if _mainObject.X > _subObject.X:
            _mainObject.X += (_right - _left)
        else:
            _mainObject.X -= (_right - _left)

def collisionMiniIntersectRect(_object1, _object2):  # 미니미니버전
    object1_x1, object1_y1, object1_x2, object1_y2 = _object1.getCollisionBox()
    object2_x1, object2_y1, object2_x2, object2_y2 = _object2.getCollisionBox()

    if object1_x1 > object2_x2: return False
    if object1_x2 < object2_x1: return False
    if object1_y2 < object2_y1: return False
    if object1_y1 > object2_y2: return False

    return True