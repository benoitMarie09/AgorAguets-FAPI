from app.schemas.actualities import ActualityRead, ActualityCreate
from app.schemas.formations import FormationRead, FormationBase, FormationCreate
from app.schemas.bundles import BundleRead, BundleBase, BundleCreate


BundleRead.update_forward_refs(FormationBase=FormationBase)
FormationRead.update_forward_refs(BundleBase=BundleBase)
BundleCreate.update_forward_refs(FormationBase=FormationBase)
FormationCreate.update_forward_refs(BundleBase=BundleBase)

