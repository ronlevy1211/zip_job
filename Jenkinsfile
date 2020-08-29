podTemplate(label: 'zipjobpod',containers: [
    containerTemplate(name: 'zipjob', image: 'ronlevy1211/zip_job', ttyEnabled: true, command: 'cat')
  ])
  {
node('zipjobpod') {
    stage('Start Zip Build'){
        container('zipjob'){
            sh """
                ###################
                ##START ZIP BUILD##
                ###################
                python3 /tmp/zip_job.py
                """
        }
    }
}
}