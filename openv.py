from onepasswordconnectsdk.client import (
    Client,
    new_client_from_environment,
)

op = new_client_from_environment()
vaults = op.get_vaults()

for vault in vaults:
    items = op.get_items(vault.id)
    for item in items:
        op_item = op.get_item(item.id, vault.id)

        exports = [x.value for x in op_item.fields if x.label == 'environment']
        password = [x.value for x in op_item.fields if x.label == 'password']
        for export in exports:
            print(f'export {export}="{password[0]}"')
