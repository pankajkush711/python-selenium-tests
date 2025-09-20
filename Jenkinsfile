pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/python-selenium-tests.git'
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    call venv\\Scripts\\activate.bat
                    pytest test_google.py --junitxml=report.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
    }
}
