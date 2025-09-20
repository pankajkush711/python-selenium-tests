pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Use your actual GitHub URL and credentials ID here
                git url: 'https://github.com/pankajkush711/python-selenium-tests.git', credentialsId: 'github-pat'
            }
        }

        stage('Set up Python') {
            steps {
                // On Windows agent, use 'bat' instead of 'sh'
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '''
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
