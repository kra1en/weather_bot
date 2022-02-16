class Queries:
    CREAT_TABLE_QUERY = """
                create table if not exists city_info(
                id int primary key,
                region varchar(100) not null,
                municipality varchar(100) not null,
                settlement varchar(100) not null,
                lat real not null, 
                lon real not null,
                UNIQUE(settlement, region));
        """
    INSERT_DATA_QUERY = """
            insert into city_info (id, region, municipality, settlement, lat, lon) 
            values (?,?,?,?,?,?) ON CONFLICT DO NOTHING;
        """
    SELECT_SETTLEMENTS_QUERY = """
            select c1.id, c1.settlement, c1.region 
            from city_info c1 where c1.settlement like (?) or c1.settlement like (?) or c1.settlement like (?) LIMIT 25;
        """
    GET_COORDINATES_BY_ID_QUERY = """
        select lat, lon from city_info
        where id = (?);
    """