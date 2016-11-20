# coding: cp949
def collisionIntersectRect(_object1, _object2):  # ���ͼ���Ʈ ������Ʈ �ΰ�
                                                 # ��ü �� �̷��� �ϴ��� �𸣰���
    # ����Ʈ ž ����Ʈ ����
    object1_x1, object1_y1, object1_x2, object1_y2 = _object1.getCollisionBox()  # ������Ʈ1 X, Y��
    object2_x1, object2_y1, object2_x2, object2_y2 = _object2.getCollisionBox()  # ������Ʈ2 X, Y��
    object3_x1, object3_y1, object3_x2, object3_y2 = 0, 0, 0, 0                  # ������Ʈ3 X, Y�� = 0
                                                                                 # �� �̷��� ������

    if (object1_y1 >= object2_y2) and (object1_x2 >= object2_x1) �
            and (object1_x1 <= object2_x2) and (object1_y2 <= object2_y1):  # ������Ʈ1�� ž�� ������Ʈ2�� ���Һ��� ũ��
                                                                             # ������Ʈ1�� ����Ʈ�� ������Ʈ2�� ����Ʈ���� ũ��
                                                                             # ������Ʈ1�� ����Ʈ�� ������Ʈ2�� ����Ʈ���� �۰�
                                                                             # ������Ʈ1�� ������ ������Ʈ2�� ž���� ���� ��
                                                                             # �� �Ҹ���
        #top
        if object1_y1 < object2_y1:         # ������Ʈ1�� ž�� ������Ʈ2�� ž���� ���� ��
            object3_y1 = object1_y1         # ������Ʈ3�� ž = ������Ʈ 1�� ž
        elif object1_y1 >= object2_y1:      # ������Ʈ1�� ž�� ������Ʈ2�� ž���� Ŭ ��
            object3_y1 = object2_y1         # ������Ʈ3�� ž = ������Ʈ 2�� ž
                                            # ���� ž�� ������Ʈ3�� ž���� �Ѱ��ش�
        #bottom
        if object1_y2 > object2_y2:         # ������Ʈ1�� ������ ������Ʈ2�� ���Һ��� Ŭ ��
            object3_y2 = object1_y2         # ������Ʈ3�� ���� = ������Ʈ1�� ����
        elif object1_y2 <= object2_y2:     # ������Ʈ1�� ������ ������Ʈ2�� ���Һ��� ���� ��
            object3_y2 = object2_y2         # ������Ʈ3�� ���� = ������Ʈ2�� ����
                                            # ū ������ ������Ʈ3�� ���ҿ� �Ѱ��ش�
        #right
        if object1_x2 < object2_x2:         # ������Ʈ1�� ����Ʈ�� ������Ʈ2�� ����Ʈ���� ���� ��
            object3_x2 = object1_x2         # ������Ʈ3�� ����Ʈ = ������Ʈ1�� ����Ʈ
        elif object1_x2 >= object2_x2:      # ������Ʈ1�� ����Ʈ�� ������Ʈ2�� ����Ʈ���� Ŭ ��
            object3_x2 = object2_x2         # ������Ʈ3�� ����Ʈ = ������Ʈ2�� ����Ʈ
                                            # ���� ����Ʈ�� ������Ʈ3�� ����Ʈ�� �Ѱ��ش�
        #left
        if object1_x1 > object2_x1:         # ������Ʈ1�� ����Ʈ�� ������Ʈ2�� ����Ʈ���� Ŭ ��
            object3_x1 = object1_x1         # ������Ʈ3�� ����Ʈ = ������Ʈ1�� ����Ʈ
        elif object1_x1 <= object2_x1:      # ������Ʈ1�� ����Ʈ�� ������Ʈ2�� ����Ʈ���� ���� ��
            object3_x1 = object2_x1         # ������Ʈ3�� ����Ʈ = ������Ʈ2�� ����Ʈ
                                            # ū ����Ʈ�� ������Ʈ3�� ����Ʈ�� �Ѱ��ش�
        return True, object3_x1, object3_y1, object3_x2, object3_y2  # �ٲ� ������Ʈ3�� �� �ѱ��
    return False, object3_x1, object3_y1, object3_x2, object3_y2    # 0�� ������Ʈ3�� �� �ѱ��

def collisionPtInRect(_object, _x, _y):  # ��Ƽ�η�Ʈ ������Ʈ �Ѱ�, x, y��
    if (_object.X - (int)(_object.sizeX / 2) <= _x) and (_object.X + (int)(_object.sizeX / 2) >= _x):
        if (_object.Y - (int)(_object.sizeY / 2) <= _y) and (_object.Y + (int)(_object.sizeY / 2) >= _y):
            # ������Ʈ �ȿ� _x, _y�� ���� ��
            return True
    return False

def collisionAABB(_mainObject, _subObject, _left, _top, _right, _bottom):
    # ���� ������Ʈ, ���������Ʈ, ����Ʈ ž ����Ʈ ����
    # ������Ʈ3
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

def collisionMiniIntersectRect(_object1, _object2):  # �̴Ϲ̴Ϲ���
    object1_x1, object1_y1, object1_x2, object1_y2 = _object1.getCollisionBox()
    object2_x1, object2_y1, object2_x2, object2_y2 = _object2.getCollisionBox()

    if object1_x1 > object2_x2: return False
    if object1_x2 < object2_x1: return False
    if object1_y2 < object2_y1: return False
    if object1_y1 > object2_y2: return False

    return True