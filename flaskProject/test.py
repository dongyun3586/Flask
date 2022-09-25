import test_pkg.operation  # test_pkg 패키지의 operation 모듈을 가져옴
import test_pkg.geometry  # test_pkg 패키지의 geometry 모듈을 가져옴

print(test_pkg.operation.add(10, 20))  # operation 모듈의 add 함수 사용
print(test_pkg.operation.mul(10, 20))  # operation 모듈의 mul 함수 사용

print(test_pkg.geometry.triangle_area(30, 40))  # geometry 모듈의 triangle_area 함수 사용
print(test_pkg.geometry.rectangle_area(30, 40))  # geometry 모듈의 rectangle_area 함수 사용