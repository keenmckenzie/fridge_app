package com.mckenzie.fridge.repository;

import com.mckenzie.fridge.model.Item;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Date;
import java.util.List;
import java.util.Optional;

@Repository
public interface ItemRepository extends JpaRepository<Item, Long> {
    Optional<Item> findByNameIgnoreCase(String name);

    List<Item> findByExpirationDateBetween(Date startDate, Date endDate);

}
