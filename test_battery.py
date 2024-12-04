import pytest #type: ignore
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b


def describe_Battery():

    def describe_recharge():
        # your test cases here
        def it_recharges_to_capacity_from_partial_charge():
            b = Battery(100)
            assert b.getCharge() == 100
            b.mCharge = 70
            assert b.getCharge() == 70
            b.recharge(30)
            assert b.getCharge() == 100
        
        def it_doesnt_overcharge():
            b = Battery(100)
            b.recharge(10)
            assert b.getCharge() == 100
        
        def it_doesnt_charge_negative():
            b = Battery(100)
            b.recharge(-10)
            assert b.getCharge() == 100

        def it_doesnt_charge_0():
            b = Battery(100)
            b.recharge(0)
            assert b.getCharge() == 100

        def it_notifies_external_monitor():
            b = Battery(100)
            b.mCharge = 40
            mock_monitor = Mock()
            b.external_monitor = mock_monitor
            b.recharge(30)
            mock_monitor.notify_recharge.assert_called_once_with(70)

    def describe_drain():
        # your test cases here
        def it_drains_partially():
            b = Battery(100)
            b.drain(30)
            assert b.getCharge() == 70

        def it_drains_to_0():
            b = Battery(100)
            b.drain(100)
            assert b.getCharge() == 0
        
        def it_doesnt_drain_negative():
            b = Battery(100)
            b.drain(-10)
            assert b.getCharge() == 100

        def it_doesnt_drain_0():
            b = Battery(100)
            b.drain(0)
            assert b.getCharge() == 100

        def it_notifies_external_monitor():
            b = Battery(100)
            mock_monitor = Mock()
            b.external_monitor = mock_monitor
            b.drain(30)
            mock_monitor.notify_drain.assert_called_once_with(70)
        