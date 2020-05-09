package com.mckenzie.fridge.controller;

import com.mckenzie.fridge.model.Recipe;
import com.mckenzie.fridge.repository.RecipeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/recipes")
public class RecipeController {
    @Autowired
    RecipeRepository recipeRepository;

    @GetMapping("/")
    public List<Recipe> getAllRecipes(){
        return recipeRepository.findAll();
    }

    @PostMapping("/")
    public Recipe createItem(@Valid @RequestBody Recipe recipe) {
        return recipeRepository.save(recipe);
    }
}
