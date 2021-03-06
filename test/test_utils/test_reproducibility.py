import torch

from homura import set_seed, set_deterministic


def test_reproducibility():
    with set_seed():
        a = torch.randn(3, 3)
        b = torch.randn(4, 3)

    with set_seed(0):
        assert torch.equal(a, torch.randn(3, 3))
        assert torch.equal(b, torch.randn(4, 3))

    assert not torch.equal(a, torch.randn(3, 3))

    with set_deterministic():
        assert not torch.backends.cudnn.benchmark
    assert torch.backends.cudnn.benchmark
