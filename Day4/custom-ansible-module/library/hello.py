from ansible.module_utils.basic import AnsibleModule

def sayHello(msg):
    return "Hello Custom Module message - " + msg + " !"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(type='str'),
        )
    )

    msg = module.params['message']

    result = dict(
        output= sayHello(msg),
    )

    #This must be called when went well and no changes were involved, 
    #if module has made some changes, then we must say changed=True so that ansible reports in yellow color 
    module.exit_json(**result,changed=False)

    #This must be called when there is a failure
    #module.fail_json(msg="Some unknown error occurred")

if __name__ == '__main__':
    main()
