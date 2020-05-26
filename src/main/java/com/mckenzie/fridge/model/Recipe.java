package com.mckenzie.fridge.model;

import javax.persistence.*;
import javax.validation.constraints.NotBlank;
import java.util.List;
import java.util.Set;

@Entity
@Table(name = "recipes")
public class Recipe {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", unique = true, nullable = false)
    private Long recipeId;

    @NotBlank
    private String name;

    /*
    @NotBlank
    @OneToMany(mappedBy = "recipe")
    private List<Ingredient> ingredients;
     */

    @ManyToMany(cascade=CascadeType.ALL)
    @JoinTable(name="recipe_ingredients", joinColumns={@JoinColumn(referencedColumnName="id")}
            , inverseJoinColumns={@JoinColumn(referencedColumnName="id")})
    private Set<Ingredient> ingredients;

    public Long getRecipe_id() {
        return recipeId;
    }

    public void setRecipe_id(Long id) {
        this.recipeId = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Set<Ingredient> getIngredients() {
        return ingredients;
    }

    public void setIngredients(Set<Ingredient> ingredients) {
        this.ingredients = ingredients;
    }
}
