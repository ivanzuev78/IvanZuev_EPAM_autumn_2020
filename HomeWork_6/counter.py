def instances_counter(cls):
    """
    Написать декоратор instances_counter, который применяется к любому классу
    и добавляет ему 2 метода:
    get_created_instances - возвращает количество созданых экземпляров класса
    reset_instances_counter - сбросить счетчик экземпляров,
    возвращает значение до сброса
    Имя декоратора и методов не менять
    """

    class InstancesCounterDecoratedClass(cls):
        cls._counter = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            cls._counter += 1

        @staticmethod
        def get_created_instances():
            return cls._counter

        @staticmethod
        def reset_instances_counter():
            count, cls._counter = cls._counter, 0
            return count

    return InstancesCounterDecoratedClass
