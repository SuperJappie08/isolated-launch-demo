# Isolated Launch Demo
> Package to demonstrate scoping issues with launch

1. Unintended leakage both ways: `parent_include_args_plain.launch.xml`
2. Only inwards leakage: `parent_include_args_scope_forward.launch.xml`
3. No leakage, but broken namespace: `parent_include_args_scope_no_forward.launch.xml`
4. No leakage, fixes namespace, however does not scale over extensions: `parent_include_args_scope_no_forward_fix.launch.xml`
   - Also breaks when nested: `parent_include_args_scope_no_forward_fix_error.launch.xml`

