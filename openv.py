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
        for field in op_item.fields:
            print(
                f'export {op_item.title.upper()}_{field.label.upper()}="{field.value}"')
