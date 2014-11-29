Ansible Coding Conventions
==================

## General

* YAML files - All yaml files should use 2 space indents and end with `.yaml`
* Variables - Use jinja variable syntax over deprecated variable syntax.  `{{ var }}` not `$var`
* Use spaces around jinja variable names. `{{ var }}` not `{{var}}`
* Variables that are environment specific and that need to be overridden should be in ALL CAPS.
* Variables that are internal to the role should be lowercase.
* Prefix all variables defined in a role with the name of the role. Example: `EDXAPP_FOO`
* Keep roles self contained - Roles should avoid including tasks from other roles when possible
* Plays should do nothing more than include a list of roles except where pre_tasks and post_tasks are required (to manage a load balancer for example)
* Tests - The .gitignore should ignore `*test*` to allow for local testing without polluting the repository
* Handlers - Any service requiring to restarted should be done via handlers. In other words, no hardcoded reboots of any service to include the host itself.

## Conditionals and return status

* Always use `when:` for conditionals - To check if a variable is defined `when: my_var is defined` or `when: my_var is not defined`
* To learn more  (see [conditional execution](http://docs.ansible.com/playbooks_conditionals.html#the-when-statement))

## Formatting 

Break long lines using yaml line continuation

```
  - debug: >
      msg={{ test }}
```

```
  - debug:
      msg: "{{ test }}"
```


## Roles

### Role Variables

* group_vars/all - Contains variable definitions that apply to all roles.
* "common" role - Contains variables and tasks that apply to all roles.
* Roles variables - Variables specific to a role should be defined in <role>/vars/main.yml. All variables should be prefixed with the role name.
* Variables that are environment specific and that need to be overridden should be in all caps.

### Role naming conventions 

* Role names - Terse, lowercase, one word if possible
* Role task names - Terse, descriptive, spaces are OK
* Role handlers - Terse, descriptive, spaces are OK


## Secure vs. Insecure data

As a general policy we want to protect the following data:

* Usernames (should be avoided in public repos)
* Public keys (keys are OK to be public)
* Hostnames (should never be hardcoded in play)
* Passwords, API keys (should never be hardcoded in a play)
