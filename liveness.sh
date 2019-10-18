#! /bin/bash
set -e
declare -a urls=( "http://tc-hci-accpub-mockservice:8080/ui" )
#  "http://tc-hci-accpub-id-proofing:8080/ui" 
# registration/matchFace identityProof
for url in "${urls[@]}"
do
        if curl --output /dev/null --silent --head --fail "$url"; then
                echo "URL exists: $url"
        else
                echo "URL does not exist: $url"
                exit -1
        fi
done
