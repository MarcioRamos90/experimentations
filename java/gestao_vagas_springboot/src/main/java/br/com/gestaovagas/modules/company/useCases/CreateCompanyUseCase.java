package br.com.gestaovagas.modules.company.useCases;

import java.nio.file.attribute.UserPrincipalNotFoundException;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import br.com.gestaovagas.exceptions.UserAlreadyExists;
import br.com.gestaovagas.modules.company.entities.CompanyEntity;
import br.com.gestaovagas.modules.company.repositories.CompanyRepository;


@Service
public class CreateCompanyUseCase {

    @Autowired
    private CompanyRepository companyRepository;

    public CompanyEntity execute(CompanyEntity companyEntity) {
        companyRepository.findByUsernameOrEmail(companyEntity.getUsername(), companyEntity.getEmail())
        .ifPresent((user) -> {
            throw new UserAlreadyExists();
        });

        return this.companyRepository.save(companyEntity);
    }
}
