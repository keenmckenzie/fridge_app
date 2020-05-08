package com.mckenzie.fridge.controller;

import com.mckenzie.fridge.model.Ingredient;
import com.mckenzie.fridge.repository.IngredientRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@CrossOrigin(origins = { "*" })
@RestController
@RequestMapping("/api/ingredients")
public class IngredientController {

    @Autowired
    IngredientRepository ingredientRepository;

    @GetMapping("/")
    public List<Ingredient> getAllItems() {
        return ingredientRepository.findAll();
    }

    @PostMapping("/")
    public Ingredient createItem(@Valid @RequestBody Ingredient ingredient) {
        return ingredientRepository.save(ingredient);
    }

    


}
