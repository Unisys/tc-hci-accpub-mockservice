properties([parameters([string(name: 'LIB_VERSION', defaultValue: 'develop')])])
library "jenkins-library@${params.LIB_VERSION}" // ${params.LIB_VERSION}

pythonPipeline(   appName: 'tc-hci-accpub-mockservice',
                repo: 'https://github.com/Unisys/tc-hci-accpub-mockservice.git')

