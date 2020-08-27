podTemplate(containers: [
    containerTemplate(name: 'zipjob', image: 'ronlevy1211/zip_job', ttyEnabled: true, command: 'cat'),
  ])
node {
    stage('Start Zip Build'){
        container('zipjob'){
            sh 'echo test'
        }
    }
}