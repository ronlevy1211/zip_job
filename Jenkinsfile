node {
    stage('Start Zip Build'){
        container('zip_job'){
            sh """
                python3 zip_job.py
            """
        }
    }
}