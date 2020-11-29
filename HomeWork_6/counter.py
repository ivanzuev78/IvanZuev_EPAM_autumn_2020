def instances_counter(old_cls):
    """
    Написать декоратор instances_counter, который применяется к любому классу
    и добавляет ему 2 метода:
    get_created_instances - возвращает количество созданых экземпляров класса
    reset_instances_counter - сбросить счетчик экземпляров,
    возвращает значение до сброса
    Имя декоратора и методов не менять
    """

    class InstancesCounterDecoratedClass(old_cls):
        __counter = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            InstancesCounterDecoratedClass.__counter += 1

        @classmethod
        def get_created_instances(cls):
            return cls.__counter

        @classmethod
        def reset_instances_counter(cls):
            count, cls.__counter = cls.__counter, 0
            return count

    return InstancesCounterDecoratedClass
