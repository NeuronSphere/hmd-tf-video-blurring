*** Settings ***
Library           hmd_lib_robot_shared.containers_lib.ContainerLib
Variables         tx_vars.py
Test Setup        Test Cleanup

*** Test Cases ***
Test PDF Generation
    [Documentation]    Runs built Transform Image
    Run Transform Container    ${HMD_CONTAINER_REGISTRY}/hmd-tf-video-blurring:0.1    ${tf_context}

*** Keywords ***
Test Cleanup
    No Operation
