import click, pytest, sys, jwt
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import *
from flask import jsonify

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create-user", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list-users", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format != 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())


@user_cli.command("add-review", help="creates a new student review")
@click.argument("review_id")
@click.argument("student_id")
@click.argument("content")
def create_review_command(review_id, student_id, content):
    create_review(review_id, student_id, content)
    print(f'Review added for {student_id}!')

@user_cli.command("list-reviews", help="lists all reviews")
def list_reviews_command():
    print(list_reviews())


app.cli.add_command(user_cli) # add the group to the cli


student = AppGroup('student', help='Student object commands') 

@student.command("create", help='creates a new student object')
@click.argument("stu_id")
@click.argument("stu_name")
def create_student_command(stu_id, stu_name):
    create_student(stu_id, stu_name)
    print(f'Student created!')
    return

@student.command("list", help='lists all students')
def list_students_command():
    print(get_all_students())

@student.command("update", help='updates a student according to ID')
@click.argument("stu_id")
@click.argument("name")
def update_student_command(stu_id, name):
    update_student(stu_id, name)
    print(get_student(stu_id))

@student.command("search")
@click.argument("name")
def search_student_command(name):
    print(search_student(name))


app.cli.add_command(student)

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)
