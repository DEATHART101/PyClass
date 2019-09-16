import math

class Vector2:
    m_x = 0.0
    m_y = 0.0

    def __init__(self, x, y):
        self.m_x = x
        self.m_y = y

    def __add__(self, rhs):
        return Vector2(self.m_x + rhs.m_x, self.m_y + rhs.m_y)

    def __sub__(self, rhs):
        return Vector2(self.m_x - rhs.m_x, self.m_y - rhs.m_y)

    def __mul__(self, rhs):
        return Vector2(self.m_x * rhs, self.m_y * rhs)

    def __div__(self, rhs):
        return Vector2(self.m_x / rhs, self.m_y / rhs)

    def GetMagnitude(self):
        return math.sqrt(self.m_x**2 + self.m_y**2)

    def GetArgument(self):
        if self.m_x == 0:
            if self.m_y > 0:
                return math.pi/ 2
            elif self.m_y < 0:
                return -math.pi /  2
            else:
                return 0
        else:
            return math.atan2(self.m_y, self.m_x)

    @staticmethod
    def Dot(lhs, rhs):
        return lhs.m_x * rhs.m_x + lhs.m_y * rhs.m_y

    @staticmethod
    def IMul(lhs, rhs):
        return Vector2(
            lhs.m_x * rhs.m_x + lhs.m_y * -rhs.m_y,
            lhs.m_x * rhs.m_y + lhs.m_y * rhs.m_x
        )