node {
    stage('Start Zip Build'){
        container('zipjob'){
            sh """
                python3 zip_job.py
            """
        }
    }
}