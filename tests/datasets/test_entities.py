from nanoforge.datasets import EntityFactory


def test_seed_reproducible():

    a = EntityFactory(seed=42)

    b = EntityFactory(seed=42)

    assert a.customer_id() == b.customer_id()


def test_customer_id():

    factory = EntityFactory()

    cid = factory.customer_id()

    assert "-" in cid


def test_invoice():

    factory = EntityFactory()

    invoice = factory.invoice()

    assert invoice.startswith("INV-")


def test_uuid():

    factory = EntityFactory()

    uid = factory.uuid()

    assert len(uid.split("-")) == 4


def test_email():

    factory = EntityFactory()

    email = factory.email()

    assert "@" in email


def test_name():

    factory = EntityFactory()

    assert len(factory.full_name().split()) == 2


def test_city():

    factory = EntityFactory()

    assert factory.city() in EntityFactory.CITIES