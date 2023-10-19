from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializer import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def create_direction(request):
    user = request.user
    if user.status in [2]:
        direction = Direction.objects.create(
            name=request.POST.get('name'),
            duration=request.POST.get('duration'),
            payment=request.POST.get('payment'),
        )
        data = {
            'direction': DirectionSerializer(direction).data,
            "success": True
        }
    else:
        data = {
            "success": False,
            'message': 'You are not allowed to use this function.'
        }
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def get_directions(request):
    user = request.user
    if user.status in [2, 4]:
        directions = Direction.objects.all()
        data = DirectionSerializer(directions, many=True).data
    else:
        data = {
            "success": False,
            'message': 'You are not allowed to use this function.'
        }
    return Response(data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def change_direction(request, pk):
    user = request.user
    if user.status in [2, 4]:
        name = request.POST.get('name')
        duration = request.POST.get('duration')
        payment = request.POST.get('payment')
        direction = Direction.objects.get(id=pk)
        if name is not None:
            direction.name = name
        if duration is not None:
            direction.duration = duration
        if payment is not None:
            direction.payment = payment
        direction.save()
        data = DirectionSerializer(direction, many=False).data
    else:
        data = {
            "success": False,
            'message': 'You are not allowed to use this function.'
        }
    return Response(data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def delete_direction(request, pk):
    user = request.user
    if user.status in [2, 4]:
        direction = Direction.objects.get(id=pk)
        direction.delete()
        data = {"Succesfully deleted"}
    else:
        data = {
            "success": False,
            'message': 'You are not allowed to use this function.'
        }
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def create_student(request):
    user = request.user
    if user.status in [2, 4]:
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        region = request.POST.get('region')
        address = request.POST.get('address')
        extra_phone = request.POST.get('extra_phone')
        student = Student.objects.create(full_name=full_name, phone=phone, region_id=region, address=address, extra_phone=extra_phone)
        data = StudentSerializer(student, many=False).data
    else:
        data = {
            "success": False,
            'message': 'You are not allowed to use this function.'
        }
    return Response(data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def get_students(request, pk):
    group = Group.objects.all()
    if group.filter(id=pk).count() > 0:
        this_group = Group.objects.get(id=pk)
        students = this_group.students.all()
        data = StudentSerializer(students, many=True).data
    else:
        students = Student.objects.all()
        data = StudentSerializer(students, many=True).data
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_student(request, pk):
    students = Student.objects.get(id=pk)
    user = request.user
    if user.status == 1:
        group = Group.objects.filter(mentor=user)
        for i in group:
            stud = i.students.filter(id=pk).count()
            if stud:
                data = StudentSerializer(students, many=False).data
                break
            else:
                data = {
                    "success": False,
                    'message': "You are not allowed to use this function"
                }
    else:
        data = StudentSerializer(students, many=False).data
    return Response(data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def change_student(request, pk):
    user = request.user
    if user.status in [2, 4]:
        status = request.POST.get('status')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        region = request.POST.get('region')
        address = request.POST.get('address')
        extra_phone = request.POST.get('extra_phone')
        debt = request.POST.get('debt')
        student = Student.objects.get(id=pk)
        if status is not None:
            student.status = status
        if full_name is not None:
            student.full_name = full_name
        if phone is not None:
            student.phone = phone
        if region is not None:
            student.region = region
        if address is not None:
            student.address = address
        if extra_phone is not None:
            student.extra_phone = extra_phone
        if debt is not None:
            student.debt = debt
        student.save()
        data = StudentSerializer(student, many=False).data
    else:
        data = {
            "success": False,
            'message': 'You are not allowed to use this function.'
        }
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_group(request):
    user = request.user
    if user.status in [2, 4]:
        direction = request.data.get('direction')
        mentor = request.data.get('mentor')
        students = request.data.getlist('students')
        group = Group.objects.create(direction_id=direction, mentor_id=mentor)
        for i in students:
            group.students.add(Student.objects.get(id=i))
            student = Student.objects.get(id=i)
            student.status = 2
            student.save()
        data = GroupSerializer(group, many=False).data
    else:
        data = {
            "success": False,
            'message': 'You are not allowed to use this function.'
        }
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def get_groups(request):
    groups = Group.objects.all()
    data = GroupSerializer(groups, many=True).data
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def get_group(request, pk):
    group = Group.objects.get(id=pk)
    data = GroupSerializer(group, many=False).data
    return Response(data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def change_group(request, pk):
    group = Group.objects.get(id=pk)
    user = request.user
    if user.status == 1:
        if group.mentor == user:
            direction = request.POST.get('direction')
            mentor = request.POST.get('mentor')
            students = request.POST.get('students')
            group = Group.objects.get(id=pk)
            if direction is not None:
                group.direction_id = direction
            if mentor is not None:
                group.mentor_id = mentor
            if students is not None:
                group.students_id = students
            group.save()
            data = GroupSerializer(group, many=False).data
        else:
            data = {
                "success": False,
                'message': 'You are not allowed to use this function.'
            }
    else:
        direction = request.POST.get('direction')
        mentor = request.POST.get('mentor')
        students = request.POST.get('students')
        if direction is not None:
            group.direction_id = direction
        if mentor is not None:
            group.mentor_id = mentor
        if students is not None:
            group.students_id = students
        group.save()
        data = GroupSerializer(group, many=False).data
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def add_student_to_group(request, pk):
    student = Student.objects.get(id=pk)
    group = request.POST.get('group')
    the_group = Group.objects.get(id=group)
    the_group.students.add(student)
    student.status = 2
    student.save()
    the_group.save()
    data = StudentSerializer(student, many=False).data
    return Response(data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def remove_student_from_group(request, pk):
    student = Student.objects.get(id=pk)
    group_id = request.data.get('group_id')
    group = Group.objects.get(id=group_id)
    if group.students.filter(id=student.id).count() > 0:
        group.students.remove(student)
        group.save()
        student.status = 1
        student.save()
        data = GroupSerializer(group, many=False).data
    else:
        data = {
            'success': False,
            'message': "This student doesn't study in this group."
        }
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def create_region(request):
    name = request.POST['name']
    region = Region.objects.create(name=name)
    data = RegionSerializer(region, many=False).data
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def get_regions(request):
    regions = Region.objects.all()
    data = RegionSerializer(regions, many=True).data
    return Response(data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def change_region(request, pk):
    region = Region.objects.get(id=pk)
    name = request.POST.get('name')
    region.name = name
    region.save()
    data = RegionSerializer(region, many=False).data
    return Response(data)


from decimal import Decimal
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_payment(request):
    student = request.POST['student']
    money = request.POST['money']
    group = request.POST['group']
    payment = Payment.objects.create(student_id=student, money=money, group_id=group)
    student2 = Student.objects.get(id=student)
    student2.debt += Decimal(money)
    student2.save()
    data = PaymentSerializer(payment, many=False).data
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def get_payments(request):
    payments = Payment.objects.all()
    data = PaymentSerializer(payments, many=True).data
    return Response(data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def change_payment(request, pk):
    student = request.POST.get('student')
    money = request.POST.get('money')
    group = request.POST.get('group')
    payment = Payment.objects.get(id=pk)
    student2 = Student.objects.get(id=payment.student_id)
    old_money = student2.debt
    if student is not None:
        payment.student_id = student
    if money is not None:
        payment.money = money
    if group is not None:
        payment.group_id = group
    old_money -= Decimal(money)
    student2.save()
    payment.save()
    data = PaymentSerializer(payment, many=False).data
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def get_payment(request, pk):
    payment = Payment.objects.get(id=pk)
    data = PaymentSerializer(payment, many=False).data
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def get_unpayed_students(request):
    students = Student.objects.filter(debt__gt=0.00)
    data = StudentSerializer(students, many=True).data
    return Response(data)

