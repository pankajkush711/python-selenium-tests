pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Specify branch explicitly
                git branch: 'main', url: 'https://github.com/pankajkush711/python-selenium-tests.git', credentialsId: 'github-pat'
            }
        }

        stage('Set up Python') {
            steps {
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
