import pytest
import graphics.descriptor_heap_page as mod

CASES = [
    ("recycle_by_flight", (1,)),
    ("offset_device_align", (1,)),
    ("swap_on_resize", (1,)),
    ("cross_queue_barrier", (1,)),
    ("dirty_check", (1,)),
    ("grow_headroom", (1,)),
    ("alloc_page", (1,)),
    ("free_page", (1,)),
    ("bind_table", (1,)),
    ("write_desc", (1,)),
    ("validate_heap", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
