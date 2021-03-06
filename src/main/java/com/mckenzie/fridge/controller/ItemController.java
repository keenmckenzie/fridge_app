package com.mckenzie.fridge.controller;

import com.mckenzie.fridge.exception.ResourceNotFoundException;
import com.mckenzie.fridge.model.Item;
import com.mckenzie.fridge.repository.ItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

@CrossOrigin(origins = { "*" })
@RestController
@RequestMapping("/api")
public class ItemController {

    @Autowired
    ItemRepository itemRepository;

    @GetMapping("/items")
    public List<Item> getAllItems() {
        return itemRepository.findAll();
    }

    @PostMapping("/items")
    public Item createItem(@Valid @RequestBody Item item) {
        //TODO item.setExpirationDate()
        item.setExpirationDate();
        return itemRepository.save(item);
    }

    @GetMapping("/items/{id}")
    public Item getItemById(@PathVariable(value = "id") Long itemId) {
        return itemRepository.findById(itemId)
                .orElseThrow(() -> new ResourceNotFoundException("Item", "id", itemId));
    }

    @GetMapping("/itemName/{name}")
    public Item getItemById2(@PathVariable(value = "name") String name) {
        return itemRepository.findByNameIgnoreCase(name)
                .orElseThrow(() -> new ResourceNotFoundException("Item", "id", name));
    }

    @GetMapping("/items/expiring")
    public List<Item> getExpiringItems() {
        Date yesterday;
        Date tomorrow;
        Calendar calendar = Calendar.getInstance();
        calendar.add(calendar.DAY_OF_YEAR, 1);
        tomorrow = calendar.getTime();

        calendar = Calendar.getInstance();
        calendar.add(calendar.DAY_OF_YEAR, -1);

        yesterday = calendar.getTime();

        return itemRepository.findByExpirationDateBetween(yesterday, tomorrow);
    }

    @PutMapping("/items/{id}")
    public Item updateNote(@PathVariable(value = "id") Long itemId,
                           @Valid @RequestBody Item itemDetails) {

        Item item = itemRepository.findById(itemId)
                .orElseThrow(() -> new ResourceNotFoundException("Item", "id", itemId));

        item.setName(itemDetails.getName());
        item.setCount(itemDetails.getCount());
        item.updateExpirationDate(itemDetails.getExpirationDate());


        Item updatedItem = itemRepository.save(item);
        return updatedItem;
    }

    @DeleteMapping("/items/{id}")
    public ResponseEntity<?> deleteItem(@PathVariable(value = "id") Long itemId) {
        Item item = itemRepository.findById(itemId)
                .orElseThrow(() -> new ResourceNotFoundException("Item", "id", itemId));

        itemRepository.delete(item);

        return ResponseEntity.ok().build();
    }

    @DeleteMapping("/itemName/{name}")
    public ResponseEntity<?> deleteItemByName(@PathVariable(value = "name") String name) {
        Item item = itemRepository.findByNameIgnoreCase(name)
                .orElseThrow(() -> new ResourceNotFoundException("Item", "id", name));

        itemRepository.delete(item);

        return ResponseEntity.ok().build();
    }
}
