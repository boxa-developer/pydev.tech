from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http.response import JsonResponse, HttpResponse
from .queries import *
from loguru import logger


# -------- Config API -----------
@csrf_exempt
@api_view(['POST'])
def set_base_salary(request):
    print(request.data)
    data = request.data
    r_id = insert("""
        INSERT INTO salary.config
            (salary_base)
        VALUES
            ({})
        RETURNING id;
    """.format(data["base"]))

    logger.success(f"Setting Up BaseSalary ")

    return JsonResponse("success", safe=False)


@api_view(['GET'])
def get_base_salary(request):
    base_salary = select_query("""
        SELECT salary_base FROM salary.config;
    """)
    send_data = {
        'base_salary': base_salary[-1][0],
        "status": 200,
        "message": "success"
    }
    return JsonResponse(send_data, safe=False)


# ----------  Account Views ----------------
@csrf_exempt
@api_view(['POST'])
def add_account(request):
    data = request.data

    returning_id = insert("""
        INSERT INTO salary.employees
            (surname, name, position)
        VALUES
            ('{}', '{}', '{}')
        RETURNING id;        
    """.format(data["surname"], data["name"], data["position"]))
    logger.success(f"Employee added id:{returning_id}.")

    r_x = insert("""
        UPDATE salary.employees  SET 
            salary = {}+ (select (select salary_base from salary.config  where id=1)*p.score salary 
        from 
            salary.positions p
        where p.position = '{}')
        WHERE id={}
    returning salary;
        """.format(data['bonus'], data['position'], returning_id[0][0]))
    logger.success(f"Employee set  salary:{r_x[0][0]}.")
    send_data = {
        "status": 200,
        "message": "SUCCESS"
    }
    return JsonResponse(send_data, safe=False)


@csrf_exempt
@api_view(['GET'])
def retrieve_accounts(request):
    send_data = []
    query_data = select_query("""
        select name, surname, position, salary from salary.employees
    """)
    print(query_data)
    for row in query_data:
        (name, surname, position, salary) = row
        send_data.append(dict(
            name=name,
            surname=surname,
            position=position,
            salary=salary))
    print(send_data)

    return JsonResponse(send_data, safe=False)


@csrf_exempt
@api_view(['PUT'])
def edit_account(request):
    data = request.data

    returning_id = update("""
        UPDATE employees SET
            name = '{}',
            surname = '{}',
            position_id = {},
    """.format(data["name"], data["surname"], data["position_id"]))

    logger.success(f"Employee updated id:{returning_id}.")
    send_data = {
        "status": 200,
        "message": "SUCCESS"
    }
    return JsonResponse(send_data, safe=False)


@csrf_exempt
@api_view(['DELETE'])
def delete_account(request):
    data = request.data

    delete("""
        DELETE FROM employees
        WHERE name = '{}' and surname = '{}';
    """.format(data["name"], data["surname"]))

    send_data = {
        "status": 200,
        "message": "SUCCESS"
    }
    return JsonResponse(send_data, safe=False)


# ----------- Positions Views --------------
@api_view(['GET'])
def get_positions(request):
    positions = select_query("""
            select position, score from salary.positions
        """)
    positions = [dict(position=positions[i][0], score=positions[i][1]) for i in range(len(positions))]
    return JsonResponse(positions, safe=False)


@csrf_exempt
@api_view(['POST'])
def add_position(request):
    data = request.data
    print(data)
    positions = select_query("""
        select position from salary.positions
    """)

    positions = [str(positions[i][0]).upper() for i in range(len(positions))]
    print(positions)
    if str(data["position"]).upper() not in positions:
        r_id = insert("""
            insert into salary.positions (position, score)
            values ('{}', {})
            returning id;
        """.format(data["position"], data["score"]))
        logger.success(f"Successfully Added Position {r_id[0][0]}-position")
        status = 200
        message = "success"
    else:
        logger.info(f"Duplicate Error")
        status = 203
        message = "exists"

    send_data = {
        "status": status,
        "message": message
    }
    return JsonResponse(send_data, safe=False)


@csrf_exempt
@api_view(['PUT'])
def update_position(request):
    send_data = {
        "status": 200,
        "message": "SUCCESS"
    }
    return JsonResponse(send_data, safe=False)


@csrf_exempt
@api_view(['DELETE'])
def delete_position(request):
    send_data = {
        "status": 200,
        "message": "SUCCESS"
    }
    return JsonResponse(send_data, safe=False)


# ----------------- Bonuses Views ------------------
@api_view(['GET'])
def get_bonuses(request):
    bonuses = select_query("""
            select bonus, value from salary.bonuses
        """)
    bonuses = [dict(bonus=bonuses[i][0], value=bonuses[i][1]) for i in range(len(bonuses))]
    return JsonResponse(bonuses, safe=False)


@api_view(['POST'])
def add_bonus(request):
    data = request.data
    bonuses = select_query("""
        select bonus from salary.bonuses
    """)

    bonuses = [str(bonuses[i][0]).upper() for i in range(len(bonuses))]

    if str(data["bonus"]).upper() not in bonuses:
        r_id = insert("""
            insert into salary.bonuses (bonus, value)
            values ('{}', {})
            returning id;
        """.format(data["bonus"], data["value"]))
        logger.success(f"Successfully Added Bonus {r_id[0][0]}-bonus")
        status = 200
        message = "success"
    else:
        logger.info(f"Duplicate Error")
        status = 203
        message = "exists"

    send_data = {
        "status": status,
        "message": message
    }
    return JsonResponse(send_data, safe=False)


@csrf_exempt
@api_view(['PUT'])
def update_bonus(request):
    send_data = {
        "status": 200,
        "message": "SUCCESS"
    }
    return JsonResponse(send_data, safe=False)


@csrf_exempt
@api_view(['DELETE'])
def delete_bonus(request):
    send_data = {
        "status": 200,
        "message": "SUCCESS"
    }
    return JsonResponse(send_data, safe=False)
