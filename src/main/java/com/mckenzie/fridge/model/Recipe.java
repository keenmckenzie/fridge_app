package com.mckenzie.fridge.model;

import javax.persistence.*;
import javax.validation.constraints.NotBlank;
import java.util.List;

@Entity
@Table(name = "recipes")
public class Recipe {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long recipe_id;

    @NotBlank
    private String name;

    @NotBlank
    @OneToMany(mappedBy = "recipe")
    private List<Ingredient> ingredients;

    public Long getRecipe_id() {
        return recipe_id;
    }

    public void setRecipe_id(Long id) {
        this.recipe_id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Ingredient> getIngredients() {
        return ingredients;
    }

    public void setIngredients(List<Ingredient> ingredients) {
        this.ingredients = ingredients;
    }
}
