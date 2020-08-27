node {
    stage('Start Zip Build'){
        container('zipjob'){
            /bin/sh -c """
                python3 /tmp/zip_job.py
                echo 'Zip Build completed Successfully!'
            """
        }
    }
}