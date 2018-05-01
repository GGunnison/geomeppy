from geomeppy.geom.core_perim import core_perim_zone_coordinates

footprint_1 = [(-20, 20), (30, -30), (50, 0), (50, 65), (-25, 50)]
expected_footprint_1 = {'Perimeter_Zone_5': [(-25.0, 50.0), (-20.0, 20.0), (-15.331451032074872, 22.402518843940342), (-19.27212384434131, 46.04655571753895)],
                        'Perimeter_Zone_4': [(50.0, 65.0), (-25.0, 50.0), (-19.27212384434131, 46.04655571753895), (45.0, 58.900980486407214)],
                        'Perimeter_Zone_3': [(50.0, 0.0), (50.0, 65.0), (45.0, 58.900980486407214), (45.0, 1.513878188659973)],
                        'Perimeter_Zone_2': [(30.0, -30.0), (50.0, 0.0), (45.0, 1.513878188659973), (29.2228758492822, -22.151808037416725)],
                        'Perimeter_Zone_1': [(-20.0, 20.0), (30.0, -30.0), (29.2228758492822, -22.151808037416725), (-15.331451032074872, 22.402518843940342)],
                        'Core_Zone': [(29.2228758492822, -22.151808037416725), (45.0, 1.513878188659973), (45.0, 58.900980486407214), (-19.27212384434131, 46.04655571753895), (-15.331451032074872, 22.402518843940342)]}

footprint_2 = [(0, 0), (30, 0), (30, 20), (0, 20)]
expected_footprint_2 = {'Core_Zone': [(25.0, 5.0), (25.0, 15.0), (5.0, 15.0), (5.0, 5.0)],
                        'Perimeter_Zone_4': [(0.0, 20.0), (0.0, 0.0), (5.0, 5.0), (5.0, 15.0)],
                        'Perimeter_Zone_3': [(30.0, 20.0), (0.0, 20.0), (5.0, 15.0), (25.0, 15.0)],
                        'Perimeter_Zone_2': [(30.0, 0.0), (30.0, 20.0), (25.0, 15.0), (25.0, 5.0)],
                        'Perimeter_Zone_1': [(0.0, 0.0), (30.0, 0.0), (25.0, 5.0), (5.0, 5.0)]}


def test_core_perim():
    assert core_perim_zone_coordinates(footprint_1, 5)[0] == expected_footprint_1
    assert core_perim_zone_coordinates(footprint_2, 5)[0] == expected_footprint_2
