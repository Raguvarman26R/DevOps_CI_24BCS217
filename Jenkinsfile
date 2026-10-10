pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Online Hospital Appointment Booking System'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python source files'
                bat 'python --version'
                bat 'python -m compileall -q src tests'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests'
                bat 'python -m unittest discover -s tests -v'
            }
        }

        stage('Result') {
            steps {
                echo 'Online Hospital Appointment Booking System pipeline completed successfully'
            }
        }
    }
}