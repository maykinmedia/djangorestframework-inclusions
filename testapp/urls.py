from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import (
    CDirectNestedInclusionViewSet,
    ChildPropsViewSet,
    ChildViewSet,
    ChildViewSet2,
    ChildViewSet3,
    ContainerViewSet,
    CViewSet,
    EntryViewSet,
    EViewSet,
    MainObjectViewSet,
    ParentViewSet,
    TagViewSet,
)

router = DefaultRouter()
router.register(r"proto/tags", TagViewSet)
router.register(r"proto/parents", ParentViewSet)
router.register(r"proto/children", ChildViewSet)
router.register(r"proto/children2", ChildViewSet2, base_name="child2")
router.register(r"proto/children3", ChildViewSet3, base_name="child3")
router.register(r"proto/childconfigs", ChildPropsViewSet)
router.register(r"proto/container", ContainerViewSet)
router.register(r"proto/entries", EntryViewSet)
router.register(r"proto/c", CViewSet)
router.register(r"proto/c-nested", CDirectNestedInclusionViewSet, base_name="c-nested")
router.register(r"proto/mainobjects", MainObjectViewSet)
router.register(r"proto/e", EViewSet)


urlpatterns = [path("api/", router.urls)]
