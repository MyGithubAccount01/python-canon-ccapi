from canon_ccapi.models.devicestatus import (
    Storage,
    StorageList,
)

from canon_ccapi.protocol.versions.v100.devicestatus import (
    StorageV100,
)

from canon_ccapi.protocol.versions.v110.devicestatus import (
    StorageV110,
)

def normalize_storage_status(
    version: str,
    data: dict,
) -> StorageList:

    if version == "ver100":
        wire_data = StorageV100.model_validate(data)

        return Storage(
            storageList=[
                StorageList(
                    name=item.name,
                    contents_path=item.url,
                    access_capability=item.accesscapability,
                    max_size=item.maxsize,
                    space_size=item.spacesize,
                    contents_number=item.contentsnumber,
                )
                for item in wire_data.storagelist
            ]
        )

    elif version == "ver110":
        wire_data = StorageV110.model_validate(data)

        return Storage(
            storageList=[
                StorageList(
                    name=item.name,
                    contents_path=item.path,
                    access_capability=item.accesscapability,
                    max_size=item.maxsize,
                    space_size=item.spacesize,
                    contents_number=item.contentsnumber,
                )
                for item in wire_data.storagelist
            ]
        )

    else:
        raise NotImplementedError(
            f"Unsupported CCAPI version: {version}"
        )