import pytest
from students.models import Course, Student

@pytest.mark.django_db
def test_get_one_course(api_client, course_factory):
    course = course_factory(_quantity=3)
    first_course = course[0]
    url = f'/api/v1/courses/{first_course.id}/'
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == first_course.id

@pytest.mark.django_db
def test_get_courses(api_client, course_factory):
    course = course_factory(_quantity=3)
    url = '/api/v1/courses/'
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 3

test_data = [(i, 1) for i in range(10)]

@pytest.mark.django_db
@pytest.mark.parametrize("course_index,expected_count", test_data)
def test_filter_courses_by_id(api_client, course_factory, course_index, expected_count):
    course = course_factory(_quantity=10)
    t_course = course[course_index]
    url = f'/api/v1/courses/?id={t_course.id}'
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data[0]['id'] == t_course.id
    assert len(response.data) == expected_count

@pytest.mark.django_db
def test_filter_courses_by_name(api_client, course_factory):
    course = course_factory(_quantity=3)
    t_course = course[0]
    url = f'/api/v1/courses/?name={t_course.name}'
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data[0]['name'] == t_course.name

@pytest.mark.django_db
def test_delete_courses(api_client, course_factory):
    course = course_factory(_quantity=3)
    t_course = course[0]
    url = f'/api/v1/courses/{t_course.id}/'
    count_db = Course.objects.count()
    response = api_client.delete(url)
    assert response.status_code == 204
    check_db = Course.objects.filter(id=t_course.id).exists()
    assert check_db == False
    assert Course.objects.count() == count_db - 1

@pytest.mark.django_db
def test_create_course(api_client):
    url = f'/api/v1/courses/'
    data= {
        'name': 'test name',
    }
    count_db = Course.objects.count()
    response = api_client.post(url, data=data)
    assert response.status_code == 201
    assert response.data['name'] == 'test name'
    assert Course.objects.count() == count_db + 1

@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory(_quantity=3)
    t_course = course[0]
    data= {
        'id': t_course.id,
        'name': f'test name_{t_course.id}',
    }
    url = f'/api/v1/courses/{t_course.id}/'
    response = api_client.patch(url, data=data)
    assert response.status_code == 200
    assert response.data['name'] == f'test name_{t_course.id}'